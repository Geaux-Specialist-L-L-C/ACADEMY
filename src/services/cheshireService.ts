const CHESHIRE_API_URL = process.env.REACT_APP_CHESHIRE_API_URL || 'https://cheshire.geaux.app';
const CHESHIRE_DEBUG = process.env.REACT_APP_CHESHIRE_DEBUG === 'true';

export const logStatus = (status: string, data?: unknown): void => {
  if (CHESHIRE_DEBUG) {
    // eslint-disable-next-line no-console
    console.info(`[Cheshire API] ${status}`, data);
  }
};

export const getAvatarUrl = (userId: string): string => {
  logStatus('Fetching avatar', { userId });
  return `${CHESHIRE_API_URL}/users/${userId}/avatar`;
};
