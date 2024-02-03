
# MelodySorter

MelodySorter is a tool designed to revolutionize the way music lovers interact with their Spotify playlists. Utilizing advanced clustering algorithms, MelodySorter takes a user's Spotify playlist and organizes it into smaller, more manageable playlists based on the similarity of tracks. This innovative approach allows users to rediscover their music collection in a more organized and meaningful way, ensuring that every listening experience is perfectly tailored to their preferences. MelodySorter is ideal for Spotify users looking to enhance their music listening experience by effortlessly finding the perfect playlist for any moment.

## Installation

To get started with MelodySorter, follow these steps to install it on your system:

1. **Clone the repository**

   First, clone the MelodySorter repository to your local machine using Git. Open your terminal and run:

   ```
   git clone https://github.com/yourusername/MelodySorter.git
   ```

   Replace `yourusername` with your actual GitHub username.

2. **Set up a virtual environment (optional)**

   It's a good practice to use a virtual environment. If you don't have `virtualenv` installed, install it first:

   ```
   pip install virtualenv
   ```

   Then, create and activate a virtual environment:

   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:
     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install the dependencies**

   Navigate to the project directory and install the required dependencies:

   ```
   cd MelodySorter
   pip install -r requirements.txt
   ```

## Usage

After installing MelodySorter, you can start the process of clustering your Spotify playlists into smaller, more similar groups. Follow the steps below to use MelodySorter:

1. **Start MelodySorter**

   Run MelodySorter from your terminal. Ensure you're in the project's directory:

   ```
   python main.py
   ```

2. **Choose Your Playlist Source**

   MelodySorter will ask if you want to cluster your Liked Songs or a specific playlist. Enter `0` for Liked Songs or `1` to specify a playlist.

3. **Enter Playlist URL**

   If you choose to specify a playlist, you'll be prompted to enter its Spotify URL. Make sure you copy and paste the entire link.

4. **Track Retrieval**

   MelodySorter will retrieve all tracks from the specified source and inform you once all tracks have been successfully retrieved.

5. **Specify Sub Playlists**

   Decide on the number of sub-playlists to be generated. You can type `auto` to let MelodySorter automatically determine the optimal number or specify a number manually.

6. **Graph Visualization (Optional)**

7. **Review Generated Playlists**

   MelodySorter will display the generated sub-playlists along with a sample of tracks from each. You can review these to get an idea of how your tracks have been clustered.

8. **Adding Playlists to Spotify**

   Finally, you'll be asked if you want to add these generated playlists to your Spotify library.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License


