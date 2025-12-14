import React from 'react';
import styled from 'styled-components';

export interface CourseCardProps {
  id?: string;
  title: string;
  description: string;
  level: string;
  duration: string;
  type: string;
  category: string;
  image?: string;
}

const CourseCard: React.FC<CourseCardProps> = ({
  title,
  description,
  level,
  duration,
  type,
  category,
  image,
}) => {
  return (
    <Card>
      {image && <Thumbnail src={image} alt={title} />}
      <Content>
        <Category>{category}</Category>
        <Title>{title}</Title>
        <Description>{description}</Description>
        <Meta>
          <span>{level}</span>
          <span>{duration}</span>
          <span>{type}</span>
        </Meta>
      </Content>
    </Card>
  );
};

const Card = styled.div`
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.06);
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  }
`;

const Thumbnail = styled.img`
  width: 100%;
  height: 160px;
  object-fit: cover;
  border-radius: 10px;
`;

const Content = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const Category = styled.span`
  font-size: 0.85rem;
  color: #6c63ff;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
`;

const Title = styled.h3`
  margin: 0;
  font-size: 1.1rem;
  color: #1f1f1f;
`;

const Description = styled.p`
  margin: 0;
  color: #4a4a4a;
  font-size: 0.95rem;
  line-height: 1.4;
`;

const Meta = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.85rem;
  color: #555;
`;

export default CourseCard;
