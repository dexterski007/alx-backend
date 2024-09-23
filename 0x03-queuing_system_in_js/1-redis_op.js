import { createClient, print } from 'redis';
const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.tostring()}`)
});
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (_error, reply) => {
    console.log(reply);
  });
};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
