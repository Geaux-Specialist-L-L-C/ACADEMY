import { createTheme } from '@mui/material/styles';

export const muiTheme = createTheme({
  palette: {
    primary: {
      main: '#C29A47', // Primary gold
      dark: '#9E7D39', // Darker gold for hover states
      light: '#D4B673', // Lighter gold for accents
    },
    secondary: {
      main: '#8C6B4D', // Deep gold accent
      dark: '#725640', // Darker accent for hover states
      light: '#A68B74', // Lighter accent
    },
    background: {
      default: '#F5F3F0', // Neutral background
      paper: '#FFF8E7',   // Highlight background
    },
    text: {
      primary: '#000000', // Black
      secondary: '#666666', // Secondary text
    },
    error: {
      main: '#E74C3C',
      dark: '#C0392B',
    },
    warning: {
      main: '#F1C40F',
      dark: '#D4AC0D',
    },
    info: {
      main: '#3498DB',
      dark: '#2980B9',
    },
    success: {
      main: '#2ECC71',
      dark: '#27AE60',
    },
    divider: 'rgba(0, 0, 0, 0.12)',
  },
  breakpoints: {
    values: {
      xs: 320,
      sm: 768,
      md: 1024,
      lg: 1200,
      xl: 1536,
    },
  },
  spacing: 4, // This will multiply the spacing by 4px (MUI's default spacing unit)
});

// Create styled-components theme with the same values
export const styledTheme = {
  palette: {
    ...muiTheme.palette,
  },
  breakpoints: {
    ...muiTheme.breakpoints.values,
  },
  spacing: (factor) => `${0.25 * factor}rem`, // Keep rem units for styled-components
};
