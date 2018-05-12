library('RISmed')
library(readr)

sentences <- read_csv("~/Documents/GitHub/GNBR_api/data/neo4j/import/sentences.csv")

documents <- sentences[['pmid']]
pmids <- unique(documents)
rm(sentences)
rm(documents)

t1 <- proc.time()
N <- 50000
dates_out <- list()
pmids_out <- list()
for (i in seq(1, N, 200) ){
  k <- i + 199
  if (k > N){
    k <- N
  }
  docs <- EUtilsGet(pmids[i:k])
  dates <- YearPubmed(docs)
  s.idx <- length(dates_out) + 1
  e.idx <- s.idx + length(dates) - 1
  dates_out[s.idx:e.idx] <- dates
  pmids_out[s.idx:e.idx] <- PMID(docs)
  Sys.sleep(0.3)
}
print(proc.time() - t1)
output <- data.frame(pmid=unlist(pmids_out),
                     year=unlist(dates_out)
                     )
write.csv(output, "~/pub_year.csv", row.names = F)
# pmids[833]
