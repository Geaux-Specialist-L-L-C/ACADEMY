// File: /geaux-academy/geaux-academy/src/components/shared/Button.tsx
// Description: A reusable button component that accepts label, onClick, and disabled props.
// Author: [Your Name]
// Created: [Date]

import React from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
  disabled?: boolean;
}

const Button: React.FC<ButtonProps> = ({ label, onClick, disabled = false }) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`px-4 py-2 rounded-lg ${disabled ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 hover:bg-blue-700'}`}
    >
      {label}
    </button>
  );
};

export default Button;