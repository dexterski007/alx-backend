import { createClient, print } from 'redis';
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`)
});
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

function getHash() {
  client.HGETALL('HolbertonSchools', (_error, reply) => {
    console.log(reply);
  });
};

const entries = {
    Portland:50,
    Seattle:80,
    'New York':20,
    Bogota:20,
    Cali:40,
    Paris:2,
}

function setHash() {
  for (const [key, value] of Object.entries(entries)) {
    client.HSET('HolbertonSchools', key, value, print);
  }
  getHash();
};

setHash();
