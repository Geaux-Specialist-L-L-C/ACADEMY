// File: /src/pages/Profile.tsx
// Description: Displays user profile information and includes components for editing the profile.
// Author: [Your Name]
// Created: [Date]

import React from "react";
import { useAuth } from "../hooks/useAuth";
import ProfileCard from "../components/shared/ProfileCard";
import Button from "../components/shared/Button";

const Profile: React.FC = () => {
  const { user, logout } = useAuth();

  return (
    <div className="profile-container">
      {user ? (
        <>
          <ProfileCard 
            name={user.name} 
            bio={user.bio} 
            avatarUrl={user.avatarUrl} 
          />
          <Button label="Edit Profile" onClick={() => {/* handle edit */}} />
          <Button label="Logout" onClick={logout} disabled={false} />
        </>
      ) : (
        <p>Please log in to view your profile.</p>
      )}
    </div>
  );
};

export default Profile;