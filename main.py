from flask import Flask, render_template, request, redirect
import sqlite3
from gene_addresses import generate_btc_address, generate_ltc_address, generate_doge_address

app = Flask(__name__)


conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Check if the addresses table already exists
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='addresses'")
if not c.fetchone():
    # Create the addresses table if it does not exist
    c.execute('''CREATE TABLE addresses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  currency TEXT,
                  address TEXT)''')

conn.commit()
c.close()
conn.close()

# Define the API endpoints for each crypto coin


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/select-coin', methods=['POST'])
def select_coin():
    coin = request.form['coin']
    if coin == 'btc':
        return redirect('/btc-address?coin=btc')
    elif coin == 'eth':
        return redirect('/eth-address?coin=eth')
    elif coin == 'ltc':
        return redirect('/ltc-address?coin=ltc')
    elif coin == 'doge':
        return redirect('/doge-address?coin=goge')


@app.route('/btc-address')
def get_btc_address():
    coin = "BTC"
    btc_address, btc_private_key = generate_btc_address()
    address = btc_address
    try:
        # Store the address in the database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO addresses (currency, address) VALUES (?, ?)', (coin, address))
        conn.commit()
        c.close()
        conn.close()

        # Return the generated address to the client
        return render_template('generate_address.html', address=address, coin=coin)

    except Exception as e:
        # Log the error
        print(f'Error generating address: {e}')

        # Return an error response to the client
        return 'Error generating address', 500


@app.route('/eth-address')
def get_eth_address():
    coin = "ETH"
    eth_address, eth_private_key = generate_btc_address()
    address = eth_address
    try:
        # Store the address in the database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO addresses (currency, address) VALUES (?, ?)', (coin, address))
        conn.commit()
        c.close()
        conn.close()

        # Return the generated address to the client
        return render_template('generate_address.html', address=address, coin=coin)

    except Exception as e:
        # Log the error
        print(f'Error generating address: {e}')

        # Return an error response to the client
        return 'Error generating address', 500


@app.route('/ltc-address')
def get_ltc_address():
    coin = "LTC"
    ltc_address, ltc_private_key = generate_ltc_address()
    address = ltc_address
    try:
        # Store the address in the database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO addresses (currency, address) VALUES (?, ?)', (coin, address))
        conn.commit()
        c.close()
        conn.close()

        # Return the generated address to the client
        return render_template('generate_address.html', address=address, coin=coin)

    except Exception as e:
        # Log the error
        print(f'Error generating address: {e}')

        # Return an error response to the client
        return 'Error generating address', 500


@app.route('/doge-address')
def get_doge_address():
    coin = "DOGE"
    doge_address, doge_private_key = generate_doge_address()
    address = doge_address
    try:
        # Store the address in the database
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute(
            'INSERT INTO addresses (currency, address) VALUES (?, ?)', (coin, address))
        conn.commit()
        c.close()
        conn.close()

        # Return the generated address to the client
        return render_template('generate_address.html', address=address, coin=coin)

    except Exception as e:
        # Log the error
        print(f'Error generating address: {e}')

        # Return an error response to the client
        return 'Error generating address', 500


@app.route('/addresses', methods=['GET'])
def list_addresses():
    try:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()

        # Retrieve all addresses from the database
        c.execute('SELECT * FROM addresses')
        addresses = c.fetchall()

        # Close the database connection
        c.close()
        conn.close()

        # Return a list of addresses in a JSON response
        return {'addresses': addresses}

    except Exception as e:
        # Log the error
        print(f'Error listing addresses: {e}')

        # Return an error response to the client
        return 'Error listing addresses', 500


@app.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    try:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()

        # Retrieve the address with the specified ID from the database
        c.execute('SELECT address FROM addresses WHERE id = ?', (id,))
        address = c.fetchone()

        # Close the database connection
        c.close()
        conn.close()

        # Check if the address was found
        if address is not None:
            # Return the address in a JSON response
            return {'address': address}
        else:
            # Return an error response to the client
            return 'Address not found', 404

    except Exception as e:
        # Log the error
        print(f'Error retrieving address: {e}')

        # Return an error response to the client
        return 'Error retrieving address', 500


# start the server
if __name__ == '__main__':
    app.run(debug=True)
