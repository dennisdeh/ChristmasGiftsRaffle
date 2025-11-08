## 🎅 Christmas Gifts Raffle - Secret Santa PIN Shuffler

A little self-hosted Dockerised Python app for running a Secret Santa draw the nerdy way — right from your own server or laptop.

Each participant gets a unique PIN, defined in main.py, which runs a StreamLit app. When the app runs, all PINs are shuffled (using a controllable random seed), and when a participant enters their valid PIN, they’re shown the name of the person they’re giving a gift to.



### How It Works

Define all participants and their unique PINs in main.py.

The app shuffles everyone’s PINs — the order is reproducible using a random seed.

Each participant enters their PIN into the app.

The app reveals the recipient’s name — only to them!

No spreadsheets, no awkward spoilers.

Ho ho ho

### Running with Docker
1. Set the streamlit host port in `.env` file if you want to change it; default is 2995
2. Build and run the image: `docker compose up --build`
3. Go to [http://localhost:2995/](http://localhost:2995/) (or whatever you set the host port to) to open the app on your local machine
4. Ho ho ho

### ⚙️ Configuring the mapping
Edit the main.py file to customize participants and seed:
```python
d = {
    "Alice": "12345678",
    "Bob": "23456789",
    "Charlie": "34567890"
}
```
The mapping will then be e.g.:

| Name    | PIN  | Gift Recipient |
| ------- | ---- | -------------- |
| Alice   | 12345678 | Bob            |
| Bob     | 23456789 | Charlie        |
| Charlie | 34567890 | Alice          |


The shuffling can be changed by changing the random seed in `np.random.seed(0)`

Ho ho ho
