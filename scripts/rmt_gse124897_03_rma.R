# Volet A, étape 4a — normalisation RMA SÉPARÉE PAR COHORTE (décision D1 du préenregistrement,
# https://osf.io/6htjn). Chaque cohorte est normalisée seule : la 558 ne peut pas influencer la 331.
#
# Usage (environnement R isolé, voir README) :
#   micromamba run -r ~/micromamba -n rma Rscript scripts/rmt_gse124897_03_rma.R 331
#   micromamba run -r ~/micromamba -n rma Rscript scripts/rmt_gse124897_03_rma.R 558
#
# Entrées : data/geo/GSE124897/cel/*.CEL.gz ; liste des échantillons de la cohorte
#           (derived/cohort331_samples.txt ou sealed/cohort558_samples.txt).
# Sorties : data/geo/GSE124897/rma/cohort<N>_rma.f64 (valeurs log2, float64 petit-boutiste,
#           ordre colonne : sondes variant le plus vite), _probes.txt, _samples.txt ;
#           results/rmt_gse124897/rma_sessionInfo_cohort<N>.txt (versions, versionné).

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1 || !(args[1] %in% c("331", "558"))) stop("argument attendu : 331 ou 558")
cohort <- args[1]

root <- normalizePath(file.path(dirname(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE))), ".."))
geo <- file.path(root, "data", "geo", "GSE124897")
list_file <- if (cohort == "331") file.path(geo, "derived", "cohort331_samples.txt") else
  file.path(geo, "sealed", "cohort558_samples.txt")
gsm <- readLines(list_file, warn = FALSE)
gsm <- gsm[nzchar(gsm)]

cel_all <- list.files(file.path(geo, "cel"), pattern = "\\.CEL(\\.gz)?$", full.names = TRUE, ignore.case = TRUE)
cel_gsm <- sub("_.*$", "", basename(cel_all))
idx <- match(gsm, cel_gsm)
if (anyNA(idx)) stop(sprintf("%d fichiers CEL manquants pour la cohorte %s", sum(is.na(idx)), cohort))
files <- cel_all[idx]
cat(sprintf("cohorte %s : %d fichiers CEL\n", cohort, length(files)))

suppressPackageStartupMessages({ library(affy); library(primeviewcdf) })
eset <- justRMA(filenames = basename(files), celfile.path = dirname(files[1]),
                sampleNames = gsm, normalize = TRUE, background = TRUE)
x <- exprs(eset)
stopifnot(identical(colnames(x), gsm), !anyNA(x))
cat(sprintf("matrice RMA : %d sondes x %d échantillons, étendue %.2f à %.2f\n",
            nrow(x), ncol(x), min(x), max(x)))

out <- file.path(geo, "rma")
dir.create(out, showWarnings = FALSE)
base <- file.path(out, sprintf("cohort%s_rma", cohort))
con <- file(paste0(base, ".f64"), "wb")
writeBin(as.vector(x), con, size = 8, endian = "little")
close(con)
writeLines(rownames(x), paste0(base, "_probes.txt"))
writeLines(colnames(x), paste0(base, "_samples.txt"))

res <- file.path(root, "results", "rmt_gse124897")
dir.create(res, showWarnings = FALSE, recursive = TRUE)
sink(file.path(res, sprintf("rma_sessionInfo_cohort%s.txt", cohort)))
cat(sprintf("RMA (affy::justRMA) cohorte %s seule : %d échantillons, %d sondes\n", cohort, ncol(x), nrow(x)))
cat(sprintf("Date : %s\n\n", format(Sys.time(), tz = "UTC", usetz = TRUE)))
print(sessionInfo())
sink()
cat("écrit :", paste0(base, ".f64"), "\n")
