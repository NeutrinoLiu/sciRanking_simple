Archived: migrated to https://github.com/NeutrinoLiu/API
```
sciRanking_simple
├── resp.json         # raw respond from https://chii.ai/graphql?query=query+GetRankingList+%7B+queryRankingList%28type%3A+%22anime%22%29+%7B+...SubjectSearchResult+__typename+%7D+%7D+fragment+SubjectSearchResult+on+SearchResult+%7B+scroll_id+took+timed_out+total+result+%7B+...+on+Subject+%7B+...Subject+__typename+%7D+__typename+%7D+__typename+%7D+fragment+Subject+on+Subject+%7B+id+name+nameCN+rank+type+score+scientificRank+tags+%7B+...Tag+__typename+%7D+date+__typename+%7D+fragment+Tag+on+Tag+%7B+content+userCount+confidence+__typename+%7D
├── shrank.json       # shrank list of sciRanking, bangumi id as key, sci ranking as value, null refers to no sci ranking
└── shrink.py         
```
