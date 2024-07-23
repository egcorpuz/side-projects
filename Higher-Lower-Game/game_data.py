###################### HIGHER OR LOWER GAME #############################
# Used ChatGPT to generate the dictionary
# singers = [
#     {
#         "name": "Taylor Swift",
#         "follower_count": 173_000_000,  # hypothetical follower count
#         "description": "Award-winning singer-songwriter known for her narrative songs",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Ed Sheeran",
#         "follower_count": 122_000_000,  # hypothetical follower count
#         "description": "Talented musician recognized for his heartfelt acoustic pop songs",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Adele",
#         "follower_count": 91_000_000,  # hypothetical follower count
#         "description": "Soulful vocalist famous for her emotionally resonant ballads",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Justin Bieber",
#         "follower_count": 154_000_000,  # hypothetical follower count
#         "description": "Pop sensation known for his chart-topping hits and vocal versatility",
#         "country_of_origin_of_origin": "Canada"
#     },
#     {
#         "name": "Beyoncé",
#         "follower_count": 164_000_000,  # hypothetical follower count
#         "description": "Iconic performer known for her powerful voice and empowering anthems",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Elton John",
#         "follower_count": 88_000_000,  # hypothetical follower count
#         "description": "Legendary singer-songwriter and pianist with a career spanning decades",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Lady Gaga",
#         "follower_count": 117_000_000,  # hypothetical follower count
#         "description": "Innovative artist known for her theatrical performances and pop hits",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Michael Jackson",
#         "follower_count": 123_000_000,  # hypothetical follower count
#         "description": "The King of Pop known for his groundbreaking music and electrifying performances",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Madonna",
#         "follower_count": 99_000_000,  # hypothetical follower count
#         "description": "Pop icon and cultural phenomenon known for her provocative style and hits",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Bruno Mars",
#         "follower_count": 75_000_000,  # hypothetical follower count
#         "description": "Versatile artist blending pop, R&B, and funk with infectious energy",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Rihanna",
#         "follower_count": 192_000_000,  # hypothetical follower count
#         "description": "Chart-topping singer and fashion icon known for her distinctive voice and style",
#         "country_of_origin_of_origin": "Barbados"
#     },
#     {
#         "name": "Eminem",
#         "follower_count": 87_000_000,  # hypothetical follower count
#         "description": "Rap legend known for his lyrical prowess and raw storytelling",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Whitney Houston",
#         "follower_count": 69_200_000,  # hypothetical follower count
#         "description": "Legendary vocalist known for her powerful voice and classic ballads",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Bob Dylan",
#         "follower_count": 77_700_000,  # hypothetical follower count
#         "description": "Nobel Prize-winning songwriter and influential figure in folk and rock music",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Shakira",
#         "follower_count": 94_520_000,  # hypothetical follower count
#         "description": "Latin pop sensation known for her distinctive voice and energetic performances",
#         "country_of_origin_of_origin": "Colombia"
#     },
#     {
#         "name": "David Bowie",
#         "follower_count": 61_660_000,  # hypothetical follower count
#         "description": "Iconic musician and actor known for his innovative music and style",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Ariana Grande",
#         "follower_count": 133_000_000,  # hypothetical follower count
#         "description": "Pop diva known for her powerful vocals and chart-topping hits",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Freddie Mercury",
#         "follower_count": 50_123_000,  # hypothetical follower count
#         "description": "Legendary lead vocalist of Queen known for his theatrical performances",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Katy Perry",
#         "follower_count": 90_432_000,  # hypothetical follower count
#         "description": "Pop superstar known for her catchy songs and colorful persona",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "John Lennon",
#         "follower_count": 60_666_000,  # hypothetical follower count
#         "description": "Legendary singer-songwriter and member of The Beatles",
#         "country_of_origin_of_origin": "United Kingdom"
#     },
#     {
#         "name": "Christina Aguilera",
#         "follower_count": 61_789_000,  # hypothetical follower count
#         "description": "Powerhouse vocalist known for her soulful voice and pop anthems",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "Stevie Wonder",
#         "follower_count": 51_111_000,  # hypothetical follower count
#         "description": "Musical genius known for his soul, R&B, and pop hits",
#         "country_of_origin_of_origin": "United States"
#     },
#     {
#         "name": "George Michael",
#         "follower_count": 52_367_000,  # hypothetical follower count
#         "description": "Pop icon known for his soulful voice and memorable hits",
#         "country_of_origin_of_origin": "United Kingdom"
#     }
# ]

singers = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country_of_origin': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country_of_origin': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country_of_origin': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country_of_origin': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country_of_origin': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country_of_origin': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country_of_origin': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country_of_origin': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country_of_origin': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country_of_origin': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country_of_origin': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country_of_origin': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country_of_origin': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country_of_origin': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country_of_origin': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country_of_origin': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country_of_origin': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country_of_origin': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country_of_origin': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country_of_origin': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country_of_origin': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country_of_origin': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country_of_origin': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country_of_origin': 'United States'
    }
]
