import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

const client = createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;
const init_seats = 50;

client.on('connect', async () => {
  await setAsync('available_seats', init_seats);
});

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats')
  return parseInt(seats);
}

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat');
  job.save((error) => {
    if (error) {
      return res.json ({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  })
  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
  })
})

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', async(job, done) => {
    let currSeats = await getCurrentAvailableSeats();

    if (currSeats > 0) {
      currSeats -= 1;
      await reserveSeat(currSeats);
      if (currSeats === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  })
});

app.listen(port);
