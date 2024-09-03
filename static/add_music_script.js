document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('file-input');
    const fileList = document.getElementById('file-list');
    const loadingSpinner = document.getElementById('loading-spinner'); // Reference to the spinner

    document.getElementById('upload-form').addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData();
        const files = fileInput.files;
        if (files.length === 0) return;

        Array.from(files).forEach(file => {
            formData.append('music_file', file);
        });

        // Show the loading spinner
        loadingSpinner.style.display = 'block';

        try {
            // Send the file to the server
            const response = await fetch('/add_music', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const result = await response.json();
                fileList.innerHTML = ''; // Clear the previous list
                result.saved_files.forEach(fileName => {
                    const fileItem = document.createElement('div');
                    fileItem.className = 'file-item';

                    const nameSpan = document.createElement('span');
                    nameSpan.textContent = fileName;

                    const removeButton = document.createElement('button');
                    removeButton.textContent = "Remove";
                    removeButton.onclick = () => {
                        fileItem.remove();
                    };

                    fileItem.appendChild(nameSpan);
                    fileItem.appendChild(removeButton);

                    fileList.appendChild(fileItem);
                });

                // Show Success message
                const successMessage = document.createElement('div');
                successMessage.className = 'success-message';
                successMessage.textContent = result.message;
                document.body.appendChild(successMessage);

                // Remove the message after a few seconds
                setTimeout(() => {
                    successMessage.remove();
                }, 5000);

            } else {
                console.log("Upload failed");
            }
        } catch (error) {
            console.error("Error during file upload:", error);
        } finally {
            // Hide the loading spinner
            loadingSpinner.style.display = 'none';
        }
    });
});
