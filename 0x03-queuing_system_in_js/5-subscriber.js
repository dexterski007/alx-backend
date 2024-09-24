import { createClient } from 'redis';
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`)
});
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

client.SUBSCRIBE('holberton school channel');
client.on('message', (_error, mesg) => {
  console.log(mesg);
  if (mesg === 'KILL_SERVER') {
    client.UNSUBSCRIBE();
    client.quit();
  }
});
