export default {
  hostname: '127.0.0.1',
  port: 1883,
  clientId: 'browser_' + Math.random().toString(16).substring(2, 8),
  protocol: 'mqtt',
};
