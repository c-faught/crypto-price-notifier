import click
import store_news

@click.command()

@click.option('--add', prompt='Add stock', help='Enter the stock symbol to monitor for news updates.')
def add_stock(add):
    print(f'adding: {add}')
    store_news.add_stock_to_news(add)

@click.command()

@click.option('--remove', prompt='Remove stock', help='Enter the stock symbol to remove from news updates.')
def remove_stock(remove):
    print(f'removing: {remove}')
    store_news.remove_stock_to_news(remove)

if __name__ == '__main__':
    remove_stock()



#python cli.py --stock=ESI:CT