import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
  let queue;
  before(() => {
    queue = createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display error if not array', () => {
    expect(() => createPushNotificationsJobs('test_string', queue)).to.throw('Jobs is not an array');
  });

  it('must create 2 jobs', () => {
    const jobs = [
      { phoneNumber: '4654654654', message: 'Code number 1' },
      { phoneNumber: '6465465465', message: 'Code number 2' },
      { phoneNumber: '2135454654', message: 'Code number 3' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(3);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal({ phoneNumber: '4654654654', message: 'Code number 1' });
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal({ phoneNumber: '6465465465', message: 'Code number 2' });
    expect(queue.testMode.jobs[2].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[2].data).to.deep.equal({ phoneNumber: '2135454654', message: 'Code number 3' });
  });
})
