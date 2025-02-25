// File: /geaux-academy/geaux-academy/tests/components/ProfileCard.test.tsx
// Description: Unit tests for the ProfileCard component.
// Author: [Your Name]
// Created: [Date]

import { render, screen } from "@testing-library/react";
import ProfileCard from "@/components/shared/ProfileCard";

test("renders ProfileCard with correct props", () => {
  render(<ProfileCard name="John Doe" bio="Developer" avatarUrl="/avatar.jpg" />);
  
  expect(screen.getByText("John Doe")).toBeInTheDocument();
  expect(screen.getByText("Developer")).toBeInTheDocument();
  expect(screen.getByAltText("John Doe's Avatar")).toHaveAttribute("src", "/avatar.jpg");
});

test("renders ProfileCard with missing props", () => {
  render(<ProfileCard name="" bio="" avatarUrl="" />);
  
  expect(screen.getByText("")).toBeInTheDocument();
  expect(screen.getByAltText("''s Avatar")).toHaveAttribute("src", "");
});