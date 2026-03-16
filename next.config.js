const nextConfig = require('./frontend/next.config.js');

module.exports = {
  ...nextConfig,
  // Ensure Next.js looks for pages/app in the frontend directory
  dir: './frontend',
};
