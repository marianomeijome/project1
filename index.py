import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Soulection Music</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 50px;
            background:url("https://www.toptal.com/designers/subtlepatterns/patterns/vertical-waves.png");
        }
        .banner{
            height:300px;
            background:url("https://yt3.ggpht.com/xmUijEMKjXN4mAkaoy673aodHVvGH6_7udYTAsUyyktbcuTAvnuKfDoJ-QYPCuVHAbzQbjzvnoM=w2120-fcrop64=1,00005a57ffffa5a8-nd-c0xffffffff-rj-k-no");
            background-size:cover;
            background-position:center;
            border-bottom:5px solid #666;
            padding:50px;
            background-color:#fff;
        }
        .videos{
            max-width: 80%;
        }
        #song .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #music-video {
            width: 100%;
            height: 100%;
        }
        .song-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            border-radius:4px;
            overflow:hidden;
            height:350px;
        }
        .song-tile img{
            max-height:250px;
        }
        .circle{
            width:200px;
            height:200px;
            margin: auto;
            overflow:hidden;
            border-radius:100%;
        }
 
        .song-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#music-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.song-tile', function (event) {
            var songYouTubeId = $(this).attr('data-video-yt-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + songYouTubeId + '?autoplay=1&html5=1';
            $("#music-video-container").empty().append($("<iframe></iframe>", {
              'id': 'music-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the songs when the page loads
        $(document).ready(function () {
          $('.song-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Music Video Modal -->
    <div class="modal" id="song">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="music-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Soulection</a>
            <a class="navbar-brand" href="#">About</a>
            <a class="navbar-brand" href="#">Contact</a>
            <a class="navbar-brand" href="#">Chat</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid banner">
    
    </div>
    <div class="container videos">
      {song_tiles}
    </div>
  </body>
</html>
'''

# A single song entry html template
music_tile_content = '''
<div class="col-md-4 col-lg-3 song-tile text-center" data-video-yt-id="{song_youtube_id}" data-toggle="modal" data-target="#song">
    <div class="circle">
        <img src="{cover_art_url}">
    </div>
    <h3>{song_artist}</h3>
    <h4>{song_title}</h4>
</div>
'''

def create_song_tiles_content(songs):
    # The HTML content for this section of the page
    content = ''
    for song in songs:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', song.music_video_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', song.music_video_url)
        song_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the song with its content filled in
        content += music_tile_content.format(
            song_title=song.title,
            song_artist=song.artist,
            cover_art_url=song.cover_art_url,
            song_youtube_id=song_youtube_id
        )
    return content

def open_songs_page(songs):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the song tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(song_tiles=create_song_tiles_content(songs))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
