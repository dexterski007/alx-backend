export default function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobItem of jobs) {
    const job = queue.create('push_notification_code_3', jobItem);

    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error.toString()}`);
    });
    job.on('progress', (progress, _data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    job.save();
  }
};
