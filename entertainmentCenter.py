import music
import index

daniel_caesar = music.Music("Get You, Japanese Denim",
                        "Daniel Caesar",
                        "http://res.cloudinary.com/thefader/image/upload/IMG_6801_zisbnb.jpg",
                        "https://www.youtube.com/watch?v=6rVYRiksbRE")

jerreau = music.Music("Really Got It",
                        "Jerreau Vandel",
                        "http://stereochampions.com/wp-content/uploads/2016/06/jerreau-2.jpg",
                        "https://www.youtube.com/watch?v=hWI6-y7XHWk")

sir = music.Music("something",
                        "SiR",
                        "http://www.okayplayer.com/wp-content/uploads/2015/10/sir-soulection-beats-1.jpg",
                        "https://www.youtube.com/watch?v=Y1Mmy5LcN-4")

stro = music.Music("live set",
                     "Stro Elliot",
                     "http://www.djdmac.com/blog/wp-content/uploads/2014/06/StroElliot.jpg",
                     "https://www.youtube.com/watch?v=iwMoPG5RrxI")

jmsn = music.Music("cruel intentions, hypnotized",
                          "JMSN",
                          "http://www.whudat.de/images/2016/05/JMSN-Soulection-Cruel-Intentions-Hypnotize-WHUDAT.jpg",
                          "https://www.youtube.com/watch?v=ab5svfSft4c")

ravyn = music.Music("free room, blossum dearie",
                      "Ravyn Lenae",
                      "http://s3-us-west-1.amazonaws.com/ones2watch/blog_145626621225.jpg",
                      "https://www.youtube.com/watch?v=vKOht5hmcU8")

songs = [daniel_caesar, jerreau, sir, stro, jmsn, ravyn]
index.open_songs_page(songs)
