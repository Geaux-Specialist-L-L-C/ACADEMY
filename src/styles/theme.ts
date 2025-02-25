// File: /src/styles/theme.ts
// Description: Defines the styling variables and configurations for the application.
// Author: [Your Name]
// Created: [Date]

const theme = {
  colors: {
    primary: '#4CAF50',
    secondary: '#FF5722',
    background: '#F5F5F5',
    text: '#212121',
    border: '#E0E0E0',
  },
  spacing: (factor: number) => `${0.25 * factor}rem`,
  borderRadius: '4px',
  fontSizes: {
    small: '0.875rem',
    medium: '1rem',
    large: '1.25rem',
  },
  breakpoints: {
    mobile: '576px',
    tablet: '768px',
    desktop: '992px',
  },
};

export default theme;