import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 20,
  duration: '20s',
  thresholds: {
    checks: ['rate>0.99'],
  },
};

const url = __ENV.SITE_URL;
if (!url) {
  throw new Error('SITE_URL must be set to the deployed site URL');
}

export default function () {
  const response = http.get(url);
  check(response, {
    'response status is 2xx': (res) => res.status >= 200 && res.status < 300,
  });
  sleep(1);
}
