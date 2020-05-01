from binge_watch.entity.Movie import Movie
Genre = (
    ("Comedy", "1"),
    ("Horror", "2"),
    ("Crime", "3"),
    ("Thriller", "4"),
    ("Drama", "5"),
    ("Action", "6"),
    ("War", "7"),
    ("Romantic", "8"),
)

Language =(
    ("Hindi", "1"),
    ("English", "2"),
    ("Tamil", "3"),
    ("Telugu", "4"),
    ("Kannada", "4"),
    ("Malyalam", "5"),
    ("Bnegali", "6"),
)

EntityType = {
    "movie": Movie
}

Duration = {
    "movie": (5400, 12000),
    "trailer": (120, 600),
}

search_engine_map = {
    "000514757583409455526:iiqms4r8rga":
        ["www.primevideo.com", "www.voot.com", "www.hotstar.com"],
    "000514757583409455526:yagt2t4mvex":
        ["www.netflix.com", "www.jiocinema.com", "www.zee5.com"]
}


