import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (error) => console.log('redis error', error));

const setAsync = promisify(client.SET).bind(client);
const getAsync = promisify(client.GET).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];

function getItemById(id) {
  return listProducts.find((prod) => prod.itemId === parseInt(id));
};

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock === null ? null : parseInt(stock);
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status : 'Product not found' });
  };
  const currentStock = await getCurrentReservedStockById(item.itemId) ?? item.initialAvailableQuantity;
  res.json({ ...item, currentQuantity: currentStock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  let currentStock = await getCurrentReservedStockById(item.itemId);
  currentStock = currentStock === null ? item.initialAvailableQuantity : currentStock;
  if (currentStock <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.itemId });
  }
  await reserveStockById(item.itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

app.listen(port);


