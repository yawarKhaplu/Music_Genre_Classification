document.addEventListener('DOMContentLoaded', function() {
    const audioPlayer = document.getElementById('audio-player');
    const playButton = document.getElementById('play');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const rfileList = document.getElementById('recent-music-list');

    const songs = [
        window.musicUrls.song1,
        window.musicUrls.song2,
        window.musicUrls.song3
    ];

    let currentSongIndex = 0;

    function loadSong(index) {
        const audioSource = document.getElementById('audio-source');
        audioSource.src = songs[index];
        audioPlayer.load();
    }

    function playPauseSong() {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playButton.textContent = 'Pause';
        } else {
            audioPlayer.pause();
            playButton.textContent = 'Play';
        }
    }

    function playNextSong() {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        loadSong(currentSongIndex);
        audioPlayer.play();
        playButton.textContent = 'Pause';
    }

    function playPrevSong() {
        currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
        loadSong(currentSongIndex);
        audioPlayer.play();
        playButton.textContent = 'Pause';
    }

    playButton.addEventListener('click', playPauseSong);
    nextButton.addEventListener('click', playNextSong);
    prevButton.addEventListener('click', playPrevSong);

    loadSong(currentSongIndex);








     // Update recent uploads
     async function updateRecentUploads() {
        try {
            const response = await fetch('/'); // Fetch the home page to get recent uploads
            if (response.ok) {
                const html = await response.text();
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = html;
                const recentMusicList = tempDiv.querySelector('#recent-music-list');
                rfileList.innerHTML = recentMusicList.innerHTML;
            }
        } catch (error) {
            console.error("Error fetching recent uploads:", error);
        }
    }

    // Initial load of recent uploads
    updateRecentUploads();
});
