import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Music"]
mycol = mydb["MusicData"]


Datas = [
    {
        "name": "Sing me to sleep",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741533789224960/Alan_Walker_-_Sing_Me_To_SleepMP3_160K.mp3",
        "id": 0,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a108e07c661f9fc54de9c43a"
                }
            ]
        }
    },
    {
        "name": "Fade-NCS Release",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741536591806484/Alan_Walker_-_Fade_NCS_ReleaseMP3_160K.mp3",
        "id": 1,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a108e07c661f9fc54de9c43a"
                }
            ]
        }
    },
    {
        "name": "She-NCS Release",
        "author": "Andromedik",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741544149549096/Andromedik_-_SHE_NCS_ReleaseMP3_160K.mp3",
        "id": 2,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb37db62ee361f796bef5b49a6"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2737b8d8ca1a8e14506c8f35233"
                }
            ]
        }
    },
    {
        "name": "About you-NCS Release",
        "author": "Ascence",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741547203002389/Ascence_-_About_You_NCS_ReleaseMP3_160K.mp3",
        "id": 3,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb6e50f29c671af8aff68b321d"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27335ca35166aba974dd2dd29a2"
                }
            ]
        }
    },
    {
        "name": "On & On (feat. Daniel Levi) [NCS Release]",
        "author": "Cartoon",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741549177995264/Cartoon_-_On___On_feat._Daniel_Levi_NCS_ReleaseMP3_160K.mp3",
        "id": 4,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb65d82d90b55b4dd3cbb2efd2"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273d2aaf635815c265aa1ecdecc"
                }
            ]
        }
    },
    {
        "name": "Castle [NCS Release]",
        "author": "Clarx & Harddope",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741580619284540/Clarx___Harddope_-_Castle_NCS_ReleaseMP3_160K.mp3",
        "id": 5,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb015af0621865cd5cd5046c2c"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273ba5db46f4b838ef6027e6f96"
                }
            ]
        }
    },
    {
        "name": "Invincible [NCS Release]",
        "author": "DEAF KEV ",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741667210035220/DEAF_KEV_-_Invincible_NCS_ReleaseMP3_160K.mp3",
        "id": 6,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb33b1cf2b7b544840b727865b"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27362a57823eced1cb4fd93b2c1"
                }
            ]
        }
    },
    {
        "name": " Blank [NCS Release]",
        "author": "Disfigure",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741669588205598/Disfigure_-_Blank_NCS_ReleaseMP3_160K.mp3",
        "id": 7,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2aa26cfdf3b785f171a4795c"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27352b2a3824413eefe9e33817a"
                }
            ]
        }
    },
    {
        "name": "Nekozilla [NCS Release]",
        "author": "Different Heaven",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741669626085426/Different_Heaven_-_Nekozilla_NCS_ReleaseMP3_160K.mp3",
        "id": 8,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2af8bbb74cb106ac91d31c9a"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27309065005b0fbfc4b320d05de"
                }
            ]
        }
    },
    {
        "name": "Savannah (feat. Philly K) [NCS Release]",
        "author": "Diviners",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741669626085426/Different_Heaven_-_Nekozilla_NCS_ReleaseMP3_160K.mp3",
        "id": 9,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2d530c07b6c9f629e3327175"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273b536cfb98c74558db48f8a46"
                }
            ]
        }
    },
    {
        "name": "Cloud 9 [NCS Release]",
        "author": "Itro & Tobu",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741836018974740/Itro___Tobu_-_Cloud_9_NCS_ReleaseMP3_160K.mp3",
        "id": 10,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb90533dd45388e25202c8de48"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273d6fd719531afda5f9cc0e248"
                }
            ]
        }
    },
    {
        "name": "Sky High [NCS Release]",
        "author": "Elektronomia",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741836152668201/Elektronomia_-_Sky_High_NCS_ReleaseMP3_160K.mp3",
        "id": 11,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebbd83cf91e7780f4b0a4f0687"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27394ae8395433c0c7521ac25ba"
                }
            ]
        }
    },
    {
        "name": "Where'd You Go (feat. Luna Lark) [NCS Release]",
        "author": "Julius Dreisig",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741837642170382/Julius_Dreisig_-_Where_d_You_Go_feat._Luna_LarkMP3_160K.mp3",
        "id": 12,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb942bc92abc325c9352527759"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273100fb4649eae80922bf1acbf"
                }
            ]
        }
    },
    {
        "name": "Island [NCS BEST OF]",
        "author": "Jarico",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741836840665158/Jarico_-_Island_NCS_BEST_OFMP3_160K.mp3",
        "id": 13,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27371c82efdc4e41e6d3d4a3544"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273058c78826c35cbc3d03516c1"
                }
            ]
        }
    },
    {
        "name": "Heroes Tonight (feat. Johnning) [NCS BEST OF]",
        "author": "Janji",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741837385793556/Janji_-_Heroes_Tonight_feat._Johnning_NCS_ReleaMP3_160K.mp3",
        "id": 14,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91f4bf05646262baed9ca2d"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2739b07b787123fe99fffc9c789"
                }
            ]
        }
    },
    {
        "name": "Landscape (Vlog No Copyright Music)",
        "author": "Janji",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741839517024256/Jarico_-_Landscape_NCS_BEST_OFMP3_160K.mp3",
        "id": 15,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91f4bf05646262baed9ca2d"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27328007758bd0a5ffb1a07abeb"
                }
            ]
        }
    },
    {
        "name": "Chasing Dreams [NCS Release]",
        "author": "Jim Yosef & Valentina Franco",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741840136994846/Jim_Yosef___Valentina_Franco_-_Chasing_Dreams_NCSMP3_160K.mp3",
        "id": 16,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebb1887e30b47ba6cb5e339c0e"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273c14d955611b72addabd9163c"
                }
            ]
        }
    },
    {
        "name": "Link [NCS Release]",
        "author": "Jim Yosef",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741840224813096/Jim_Yosef_-_Link_NCS_ReleaseMP3_160K.mp3",
        "id": 17,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebb1887e30b47ba6cb5e339c0e"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2734f1608584777e92bddd5c904"
                }
            ]
        }
    },
    {
        "name": "Symbolism [NCS Release]",
        "author": "Electro-Light",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741841010065418/Electro-Light_-_Symbolism_NCS_ReleaseMP3_160K.mp3",
        "id": 18,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebadb48ec72861292e4fe833f1"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273b44de5b9f5eba409dfa753e6"
                }
            ]
        }
    },
    {
        "name": "Invisible [NCS Release]",
        "author": "Julius Dreisig & Zeus X Crona",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741873582899230/Julius_Dreisig___Zeus_X_Crona_-_Invisible_NCS_RelMP3_160K.mp3",
        "id": 19,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb942bc92abc325c9352527759"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27391b709ced968e29e8f00dfe3"
                }
            ]
        }
    },
    {
        "name": "Earth [NCS Release]",
        "author": "K-391",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741894939901992/K-391_-_Earth_NCS_ReleaseMP3_160K.mp3",
        "id": 20,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebdf3029ee98c5f4fcc0a4c203"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2732ea7097370b211b8213cdb5a"
                }
            ]
        }
    },
    {
        "name": "Harpuia [NCS Release]",
        "author": "Kadenza ",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741906344869928/Kadenza_-_Harpuia_NCS_ReleaseMP3_160K.mp3",
        "id": 21,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebaad54b2cf9044587eac7acdf"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273cac40eaa1c17e52e45a8098f"
                }
            ]
        }
    },
    {
        "name": "Dreams [NCS Release]",
        "author": "Lost Sky",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741919178653716/Lost_Sky_-_Dreams_NCS_ReleaseMP3_160K.mp3",
        "id": 22,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2867e7ca4fcd254cfbbb8940"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273eb4d7af8109e201a4d438e02"
                }
            ]
        }
    },
    {
        "name": "Fearless pt.II (feat. Chris Linton) [NCS Release]",
        "author": "Lost Sky",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741949998399572/Lost_Sky_-_Fearless_pt.II_feat._Chris_Linton_NCMP3_160K.mp3",
        "id": 23,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2867e7ca4fcd254cfbbb8940"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2733be40769b1c2361cea9f0843"
                }
            ]
        }
    },
    {
        "name": "Ark [NCS Release]",
        "author": "Ship Wrek & Zookeepers",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741988191338526/Ship_Wrek___Zookeepers_-_Ark_NCS_ReleaseMP3_160K.mp3",
        "id": 24,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb98170a22353d3b9987d26031"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27303c03da08efb9051d8fae5d5"
                }
            ]
        }
    },
    {
        "name": "Where We Started (feat. Jex) [NCS Release]",
        "author": "Lost Sky",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741989177524264/Lost_Sky_-_Where_We_Started_feat._Jex_NCS_ReleaMP3_160K.mp3",
        "id": 25,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2867e7ca4fcd254cfbbb8940"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a61f22690660bd5264495524"
                }
            ]
        }
    },
    {
        "name": "Cradles [NCS Release]",
        "author": "Sub Urban",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775741999978250250/Sub_Urban_-_Cradles_NCS_ReleaseMP3_160K.mp3",
        "id": 26,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebd0019e1ad7a088651a490862"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273cec7c8ebb684882dbaf476f5"
                }
            ]
        }
    },
    {
        "name": "Feel Good [NCS Release]",
        "author": "Syn Cole",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775742022085771278/Syn_Cole_-_Feel_Good_NCS_ReleaseMP3_160K.mp3",
        "id": 27,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf144aec1f0427c0e998abb28"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2736362397987db1fbf17f3d9b5"
                }
            ]
        }
    },
    {
        "name": "Why Do I? (feat. Bri Tolani) [NCS",
        "author": "Unknown Brain",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775742053337268224/Unknown_Brain_-_Why_Do_I__feat._Bri_Tolani_NCSMP3_160K.mp3",
        "id": 28,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb03c3e89ff4bb5b6757fd38e7"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273c1d2f3c457d0ae59a7d7e4ce"
                }
            ]
        }
    },
    {
        "name": "Infinite [NCS Release]",
        "author": "Valence",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775742064893755402/Valence_-_Infinite_NCS_ReleaseMP3_160K.mp3",
        "id": 29,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebd4d282937d2f49efd4273bae"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27361cb41224d1cc9dd052a5dba"
                }
            ]
        }
    },
    {
        "name": "Mortals (feat. Laura Brehm) [NCS Release]",
        "author": "Warriyo",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/775742084321509437/Warriyo_-_Mortals_feat._Laura_Brehm_NCS_ReleaseMP3_160K.mp3",
        "id": 30,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebe36787acbe5c4dc467e581c6"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273daf19986ce2c148768f5c362"
                }
            ]
        }
    },
    {
        "name": "Alone",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782126454690938890/Alan_Walker_-_AloneMP3_128K.mp3",
        "id": 31,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273153261ff7373a171c24ab9f9"
                }
            ]
        }
    },
    {
        "name": "Look At Her Now",
        "author": "Selena Gomez",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782128984070029322/Selena_Gomez_-_Look_At_Her_Now_Official_Music_VidMP3_128K.mp3",
        "id": 32,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba5205abffd84341e5bace828"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2732abcc266597eb46f897a8666"
                }
            ]
        }
    },
    {
        "name": "I m Fakin",
        "author": "Sabrina Carpenter",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129209711001610/Sabrina_Carpenter_-_I_m_Fakin_Audio_OnlyMP3_128K.mp3",
        "id": 33,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebd546aecf1aac2633551f4c26"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273c2d8417d46ae0c823dc6463f"
                }
            ]
        }
    },
    {
        "name": "Sing me to sleep",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129242318176266/Alan_Walker_-_Sing_Me_To_SleepMP3_128K.mp3",
        "id": 34,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a108e07c661f9fc54de9c43a"
                }
            ]
        }
    },
    {
        "name": "End of time",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129275322761236/K-391__Alan_Walker___Ahrix_-_End_of_Time_OfficialMP3_128K.mp3",
        "id": 35,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27349b9fbf2345c02ca2387a357"
                }
            ]
        }
    },
    {
        "name": "Faded",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129443250503720/Alan_Walker_-_FadedMP3_128K.mp3",
        "id": 36,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a108e07c661f9fc54de9c43a"
                }
            ]
        }
    },
    {
        "name": "The Spectre",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129468789358593/Alan_Walker_-_The_SpectreMP3_128K.mp3",
        "id": 37,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a6a151ed88a170ae3a81eff5"
                }
            ]
        }
    },
    {
        "name": "Freal Luv",
        "author": "Marshmello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129488972480532/Far_East_Movement_x_Marshmello_-_Freal_Luv_ft._Chanyeol__Tinashe_Official_Video.m4a",
        "id": 38,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91af711541f8807ed7f0676"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273bc1684a7d68f275dd6db9939"
                }
            ]
        }
    },
    {
        "name": "Let Me Love You",
        "author": "DJ Snake ft Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129492180860928/DJ_Snake_-_Let_Me_Love_You_ft._Justin_Bieber_OffiMP3_128K.mp3",
        "id": 39,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf2855e25f1d9c8a20bcc85ae"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273212d776c31027c511f0ee3bc"
                }
            ]
        }
    },
    {
        "name": "Let Me Love You",
        "author": "DJ Snake ft Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129492180860928/DJ_Snake_-_Let_Me_Love_You_ft._Justin_Bieber_OffiMP3_128K.mp3",
        "id": 40,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf2855e25f1d9c8a20bcc85ae"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273212d776c31027c511f0ee3bc"
                }
            ]
        }
    },
    {
        "name": "Here With Me Feat",
        "author": "Marshmello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129612690948106/Marshmello_-_Here_With_Me_Feat._CHVRCHES_OfficialMP3_160K.mp3",
        "id": 41,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91af711541f8807ed7f0676"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273b91a6f7b2cda3f257e9ad571"
                }
            ]
        }
    },
    {
        "name": "\u00c3\u2030chame La Culpa",
        "author": "Luis Fonsi, Demi Lovato",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129660301279252/Luis_Fonsi__Demi_Lovato_-_Echame_La_Culpa_Video_OMP3_128K.mp3",
        "id": 42,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebec1cd67f4c17468f335206eb"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2736be844b5d2fc0bf743fd7647"
                }
            ]
        }
    },
    {
        "name": "Slow Down",
        "author": "Selena Gomez",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129669578424330/Selena_Gomez_-_Slow_Down_OfficialMP3_128K.mp3",
        "id": 43,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba5205abffd84341e5bace828"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273da513d25e8b3cdd4f43f7512"
                }
            ]
        }
    },
    {
        "name": "On my Way",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129671055605760/Alan_Walker__Sabrina_Carpenter___Farruko_-_On_MyMP3_128K.mp3",
        "id": 44,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273d2aaf635815c265aa1ecdecc"
                }
            ]
        }
    },
    {
        "name": "Summer",
        "author": "Marshmello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129702650773544/Marshmello_-_Summer_Official_Music_Video_with_LeMP3_160K.mp3",
        "id": 45,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91af711541f8807ed7f0676"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a111c87c210cc9bff93948bd"
                }
            ]
        }
    },
    {
        "name": "Can't Blame a Girl for Trying",
        "author": "Sabrina Carpenter",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129754987692082/Sabrina_Carpenter_-_Can_t_Blame_a_Girl_for_TryingMP3_160K.mp3",
        "id": 46,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebd546aecf1aac2633551f4c26"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735d9a77afd5c144581be1e74e"
                }
            ]
        }
    },
    {
        "name": "Baby",
        "author": "Justin Bieber ft Ludacris",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129781373272084/Justin_Bieber_-_Baby_ft._Ludacris_Official_MusicMP3_128K.mp3",
        "id": 47,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273629dc9e2e3bc20bbd7d92e4a"
                }
            ]
        }
    },
    {
        "name": "Love You Like a Love Song",
        "author": "Selena Gomez",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129797354618880/Selena_Gomez___The_Scene_-_Love_You_Like_A_Love_SoMP3_128K.mp3",
        "id": 48,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba5205abffd84341e5bace828"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2731c8193de8d62b2ffa49a09db"
                }
            ]
        }
    },
    {
        "name": "We don't talk anymore",
        "author": "Charlie Puth",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129797403770900/Charlie_Puth_-_We_Don_t_Talk_Anymore_feat._SelenaMP3_128K.mp3",
        "id": 49,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb894f1e165ee9c04daa82a5b6"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273633a2d775747bccfbcb17a45"
                }
            ]
        }
    },
    {
        "name": "Despacito",
        "author": "Justin Bieber & Luis foni ",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129852181381121/Justin_Bieber_Despacito_Lyrics_--_ft._Luis_FonMP3_128K.mp3",
        "id": 50,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273ef0d4234e1a645740f77d59c"
                }
            ]
        }
    },
    {
        "name": "Yummy",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129879637950464/Justin_Bieber_-_Yummy_Official_VideoMP3_128K.mp3",
        "id": 51,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2737fe4a82a08c4f0decbeddbc6"
                }
            ]
        }
    },
    {
        "name": "PLAY",
        "author": "Alan Walker ft Tungevaag",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129886810603530/Alan_Walker__K-391__Tungevaag__Mangoo_-_PLAY_AlanMP3_160K.mp3",
        "id": 52,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2733899712512f50a8d9e01e951"
                }
            ]
        }
    },
    {
        "name": "Girls Like You",
        "author": "Maroon 5",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129896729214982/Maroon_5_-_Girls_Like_You_Lyrics_ft._Cardi_BMP3_128K.mp3",
        "id": 53,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb288ac05481cedc5bddb5b11b"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273deae7d931928fc1543e70203"
                }
            ]
        }
    },
    {
        "name": "Alone pt II/2 ",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129915348385822/Alan_Walker___Ava_Max_-_Alone__Pt._IIMP3_128K.mp3",
        "id": 54,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273c7870db6e559380bbc80fee8"
                }
            ]
        }
    },
    {
        "name": "Mistletoe",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129951695962142/Justin_Bieber_-_Mistletoe_Official_Music_VideoMP3_160K.mp3",
        "id": 55,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2730315efc555d5a157b0392652"
                }
            ]
        }
    },
    {
        "name": "Me Necesita",
        "author": "PRETTYMUCH, CNCO",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129959174012928/PRETTYMUCH__CNCO_-_Me_Necesita_Official_VideoMP3_160K.mp3",
        "id": 56,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb1e52ff4cbcedeaf89c0111df"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2736fd30af95d17ad6a8a3a74ad"
                }
            ]
        }
    },
    {
        "name": "Senorita",
        "author": "Shawn_Mendes,Camila_Cabello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782129973439102986/Shawn_Mendes__Camila_Cabello_-_Senorita_LyricsMP3_160K.mp3",
        "id": 57,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb92df88d91dc5a20ed4859963"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273e6095c382c2853667c1623eb"
                }
            ]
        }
    },
    {
        "name": "Ghost",
        "author": "Au/Ra, Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130010088669204/Au_Ra__Alan_Walker_-_Ghost_Official_VideoMP3_160K.mp3",
        "id": 58,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb2eac2bd8d035f71531b0c08d"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273e6f407c7f3a0ec98845e4431"
                }
            ]
        }
    },
    {
        "name": "Sorry",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130017793998848/Justin_Bieber_-_Sorry_Official_Lyric_VideoMP3_160K.mp3",
        "id": 59,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de"
                }
            ]
        }
    },
    {
        "name": "I'll Show You",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130047695585310/Justin_Bieber_-_I_ll_Show_You_Official_Music_VideMP3_160K.mp3",
        "id": 60,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de"
                }
            ]
        }
    },
    {
        "name": "Alone",
        "author": "Marshmello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130063050014732/Marshmello_-_Alone_Official_Music_VideoMP3_160K.mp3",
        "id": 61,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91af711541f8807ed7f0676"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273153261ff7373a171c24ab9f9"
                }
            ]
        }
    },
    {
        "name": "Liar",
        "author": "Camila Cabello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130071020371978/Camila_Cabello_-_Liar_LyricsMP3_160K.mp3",
        "id": 62,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf4a0158ec2c8cc0f203761da"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2732df02f0877da45295a759f4c"
                }
            ]
        }
    },
    {
        "name": "Strongest",
        "author": "Alan Walker ,Ina Wroldsen",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130079047221268/Alan_Walker___Ina_Wroldsen_-_Strongest_LyricsMP3_160K.mp3",
        "id": 63,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735510097a6f4875a4ad7c9095"
                }
            ]
        }
    },
    {
        "name": "My Oh My",
        "author": "Camila Cabello, DaBaby",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130082893398036/Camila_Cabello_-_My_Oh_My_Lyrics_ft._DaBabyMP3_160K.mp3",
        "id": 64,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf4a0158ec2c8cc0f203761da"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735f53c0dbe5190a0af0fa28f3"
                }
            ]
        }
    },
    {
        "name": "Believer",
        "author": "Imagine Dragon",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130083555966986/Imagine_Dragons_-_Believer_LyricsMP3_160K.mp3",
        "id": 65,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb920dc1f617550de8388f368e"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735675e83f707f1d7271e5cf8a"
                }
            ]
        }
    },
    {
        "name": "Heading Home",
        "author": "Alan Walker ,Ruben",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130090208133120/Alan_Walker___Ruben_Heading_Home_Official_MusicMP3_160K.mp3",
        "id": 66,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735eab23d2260268d2fab870d0"
                }
            ]
        }
    },
    {
        "name": "Company",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130102266757120/Justin_Bieber_-_Company_Official_Music_VideoMP3_160K.mp3",
        "id": 67,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de"
                }
            ]
        }
    },
    {
        "name": "Sorry (PURPOSE : The Movement)",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130111000477756/Justin_Bieber_-_Sorry_PURPOSE___The_MovementMP3_160K.mp3",
        "id": 68,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de"
                }
            ]
        }
    },
    {
        "name": "Bad Boys for Life",
        "author": "Ritmo",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130127374385162/RITMO_Bad_Boys_For_Life_Remix___Official_MusiMP3_160K.mp3",
        "id": 69,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb4a169aee26c09b8678d3fe27"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27324147afe93bc68dfdb81209a"
                }
            ]
        }
    },
    {
        "name": "Lost Control",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130131912228874/Alan_Walker_Lost_Control_Lyrics_ft._SoranaMP3_160K.mp3",
        "id": 70,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273a108e07c661f9fc54de9c43a"
                }
            ]
        }
    },
    {
        "name": "Closer",
        "author": "The Chainsmokers",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130132722384907/The_Chainsmokers_-_Closer_Lyric_ft._HalseyMP3_128K.mp3",
        "id": 71,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb7e223c8c0a40da75838373b9"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273495ce6da9aeb159e94eaa453"
                }
            ]
        }
    },
    {
        "name": "Shameless",
        "author": "Camila Cabello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130170789101578/Camila_Cabello_-_ShamelessMP3_160K.mp3",
        "id": 72,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebf4a0158ec2c8cc0f203761da"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2735f53c0dbe5190a0af0fa28f3"
                }
            ]
        }
    },
    {
        "name": "Unity",
        "author": "Alan Walker",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130173805985792/Alan_x_Walkers_-_UnityMP3_160K.mp3",
        "id": 73,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5ebc02d416c309a68b04dc94576"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2734e14d839fbece313822fca82"
                }
            ]
        }
    },
    {
        "name": "One Less Lonely Girl",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130199692443678/Justin_Bieber_-_One_Less_Lonely_Girl_Official_MusMP3_160K.mp3",
        "id": 74,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2737c3bb9f74a98f60bdda6c9a7"
                }
            ]
        }
    },
    {
        "name": "Together",
        "author": "Marshmello",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130204519694336/Marshmello_-_Together_Official_Music_VideoMP3_160K.mp3",
        "id": 75,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba91af711541f8807ed7f0676"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273ef5fa52beccb124c5f8da8d0"
                }
            ]
        }
    },
    {
        "name": "Come & Get It",
        "author": "Selena Gomez",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130215966605332/Selena_Gomez_-_Come___Get_ItMP3_128K.mp3",
        "id": 76,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eba5205abffd84341e5bace828"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273cb16227d90152c2a5022bba1"
                }
            ]
        }
    },
    {
        "name": "Boy With Luv",
        "author": "BTS",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130258811289620/BTS____Boy_With_Luv_feat._HalMP3_160K.mp3",
        "id": 77,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb82a5d58059f81867b871d8b6"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27318d0ed4f969b376893f9a38f"
                }
            ]
        }
    },
    {
        "name": "Rockabye",
        "author": "Clean Bandit",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130262342893618/Clean_Bandit_-_Rockabye_feat._Sean_Paul___Anne-MaMP3_160K.mp3",
        "id": 78,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb7a487027eb0c10af725d5410"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2731431c3bdf16aa99f71799d95"
                }
            ]
        }
    },
    {
        "name": "Blank Space",
        "author": "Taylor Swift",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130294697885696/Taylor_Swift_-_Blank_SpaceMP3_160K.mp3",
        "id": 79,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb9e3acf1eaf3b8846e836f441"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27352b2a3824413eefe9e33817a"
                }
            ]
        }
    },
    {
        "name": "What Do You Mean",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130340311203840/Justin_Bieber_-_What_Do_You_Mean__Official_MusicMP3_160K.mp3",
        "id": 80,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b273f46b9d202509a8f7384b90de"
                }
            ]
        }
    },
    {
        "name": "As Long As You Love Me",
        "author": "Justin Bieber",
        "url": "https://cdn.discordapp.com/attachments/836516032620920833/928662227601457242/As_Long_As_You_Love_Me_-_Backstreet_Boys_Lyrics_.mp3",
        "id": 81,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b2736c20c4638a558132ba95bc39"
                }
            ]
        }
    },
    {
        "name": "Confident",
        "author": "Justin Bieber ft. Chance The Rapper",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130398385143818/Justin_Bieber_-_Confident_ft._Chance_The_Rapper_OMP3_160K.mp3",
        "id": 82,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27358ae8fddecbd2630005409c9"
                }
            ]
        }
    },
    {
        "name": "Intentions",
        "author": "Justin Bieber ft. Quavo",
        "url": "https://cdn.discordapp.com/attachments/775740994595323954/782130437514067998/Justin_Bieber_-_Intentions_ft._Quavo_Official_VidMP3_160K.mp3",
        "id": 83,
        "links": {
            "images": [
                {
                    "url": "https://i.scdn.co/image/ab6761610000e5eb8ae7f2aaa9817a704a87ea36"
                },
                {
                    "url": "https://i.scdn.co/image/ab67616d0000b27308e30ab6a058429303d75876"
                }
            ]
        }
    }
]

for i in Datas:
  mycol.insert_one(i)