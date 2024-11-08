# remote app

## DB

### tables


jokes

categories



## APIs

get

https://api.chucknorris.io/jokes/random

    {
    "icon_url" : "https://api.chucknorris.io/img/avatar/chuck-norris.png",
    "id" : "5uhtkjmMQAGbXQS2nixJ8g",
    "url" : "",
    "value" : "Chuck Norris has never eaten Hamburger Helper because Chuck Norris has never needed help. NEVER"
    }


---

get

https://api.chucknorris.io/jokes/categories

    ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]


---

get

https://api.chucknorris.io/jokes/random?category={category}

https://api.chucknorris.io/jokes/random?category=animal

    {
        "categories": [
            "animal"
        ],
        "created_at": "2020-01-05 13:42:19.104863",
        "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
        "id": "zjuwql5ns-mklqumqezlhg",
        "updated_at": "2020-01-05 13:42:19.104863",
        "url": "https://api.chucknorris.io/jokes/zjuwql5ns-mklqumqezlhg",
        "value": "Chuck Norris can skeletize a cow in two minutes."
    }



---

get

https://api.chucknorris.io/jokes/search?query={text}

https://api.chucknorris.io/jokes/search?query=cigars


    {
        "total": 12,
        "result": [
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:20.841843",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "5AdmqY9GSDWuQAEPakrOYw",
                "updated_at": "2020-01-05 13:42:20.841843",
                "url": "https://api.chucknorris.io/jokes/5AdmqY9GSDWuQAEPakrOYw",
                "value": "Chuck Norris doesn't smoke cigars. He smokes smoke grenades."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:20.841843",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "a1N-fvVQRbCpEqtCVb3bvg",
                "updated_at": "2020-01-05 13:42:20.841843",
                "url": "https://api.chucknorris.io/jokes/a1N-fvVQRbCpEqtCVb3bvg",
                "value": "Chuck Norris only smokes cigars after making love. He's a forty-a-day man."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:22.701402",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "9DIfzC0kSUyg18Fguhv2-g",
                "updated_at": "2020-01-05 13:42:22.701402",
                "url": "https://api.chucknorris.io/jokes/9DIfzC0kSUyg18Fguhv2-g",
                "value": "Norris 25:17. \"The path of the righteous man (me) is beset on all sides by the inequities of the dumbasses and the tyranny of suited girlymen. Blessed is he who, in the name of charity and good will, sends boxes of cigars and crates of beer to me. For I am truly the Mack Daddy and the killer of lost children. And I will roundhouse kick thee with great vengeance and furious anger those who attempt to look at me sideways. And you will know I am the Lord, Chuck Norris, when I lay my vengeance upon you.\""
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:23.240175",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "oAOU2HtRSzG6LZjOSp9EZQ",
                "updated_at": "2020-01-05 13:42:23.240175",
                "url": "https://api.chucknorris.io/jokes/oAOU2HtRSzG6LZjOSp9EZQ",
                "value": "Chuck Norris only smokes Havana cigars and the cigars are personaly delived to Chuck Norris by Castro."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:23.484083",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "dngfZnZ2Q0eFCgy3rO13eA",
                "updated_at": "2020-01-05 13:42:23.484083",
                "url": "https://api.chucknorris.io/jokes/dngfZnZ2Q0eFCgy3rO13eA",
                "value": "Chuck Norris recently stated that cigars taste 'considerably better' when lit off of a flaming human corpse."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:24.142371",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "wsbN3wZJTyKWkuwWsHDr4g",
                "updated_at": "2020-01-05 13:42:24.142371",
                "url": "https://api.chucknorris.io/jokes/wsbN3wZJTyKWkuwWsHDr4g",
                "value": "The average human tongue has over 2,000 taste buds. Chuck Norris' tongue only needs four: to taste beer, meat, cigars and tang."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:27.496799",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "dacA9Q4vTvG_DHETV7pxaw",
                "updated_at": "2020-01-05 13:42:27.496799",
                "url": "https://api.chucknorris.io/jokes/dacA9Q4vTvG_DHETV7pxaw",
                "value": "Everybody knows that Chuck Norris blows smoke rings when he smokes cigars. But did you know that after eating Texas Chili, he often shows-off by blowing blazing fart rings."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:27.496799",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "oLhFjz2ISEGkbLo6dhHufw",
                "updated_at": "2020-01-05 13:42:27.496799",
                "url": "https://api.chucknorris.io/jokes/oLhFjz2ISEGkbLo6dhHufw",
                "value": "When refueling his Hummer at the gas station Chuck Norris likes to smoke big fat cigars and stare at the attendant."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:28.664997",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "o6KDhhf8SreEl10InaW-WA",
                "updated_at": "2020-01-05 13:42:28.664997",
                "url": "https://api.chucknorris.io/jokes/o6KDhhf8SreEl10InaW-WA",
                "value": "Chuck Norris smokes cigars while scuba-diving."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:29.296379",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "W66jrAveToyTWuVPtNv41Q",
                "updated_at": "2020-01-05 13:42:29.296379",
                "url": "https://api.chucknorris.io/jokes/W66jrAveToyTWuVPtNv41Q",
                "value": "The Terminator movies were written specifically with Chuck Norris in mind for the title role, and was originally called the Walkernator. The only differences were that the T-800 would always wear a cowboy hat and smoke cigars."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:29.569033",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "CXwMYpBwTZalk8MT7BVxcw",
                "updated_at": "2020-01-05 13:42:29.569033",
                "url": "https://api.chucknorris.io/jokes/CXwMYpBwTZalk8MT7BVxcw",
                "value": "Chuck Norris puts out his cigars in the nearest person's eye socket."
            },
            {
                "categories": [],
                "created_at": "2020-01-05 13:42:29.855523",
                "icon_url": "https://api.chucknorris.io/img/avatar/chuck-norris.png",
                "id": "ATskphrZQ7q40p0CFLA3hg",
                "updated_at": "2020-01-05 13:42:29.855523",
                "url": "https://api.chucknorris.io/jokes/ATskphrZQ7q40p0CFLA3hg",
                "value": "When Chuck Norris was born, his Dad celebrated by lighting up cigars, one for him and one for Chuck."
            }
        ]
    }

