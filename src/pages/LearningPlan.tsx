import React, { useState } from 'react';
import { AiOutlineLoading3Quarters } from 'react-icons/ai';
import { getAIResponse } from '../services/openai';
import '../styles/LearningPlan.css';

const API_KEY = process.env.REACT_APP_OPENAI_API_KEY;

const LearningPlan: React.FC = () => {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const aiResponse = await getAIResponse(prompt);
      setResponse(aiResponse);
    } catch (error) {
      console.error('Error generating learning plan', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="learning-plan">
      <h1>AI-Powered Learning Plan Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe your learning goals"
          rows={6}
        />
        <button type="submit" disabled={loading}>
          {loading ? (
            <AiOutlineLoading3Quarters className="spin" />
          ) : (
            'Generate Plan'
          )}
        </button>
      </form>
      {response && (
        <div className="response">
          <h2>Your Personalized Learning Plan</h2>
          <p>{response}</p>
        </div>
      )}
      {API_KEY ? null : (
        <p className="warning">
          Warning: OpenAI API key is not configured. Please set REACT_APP_OPENAI_API_KEY.
        </p>
      )}
    </div>
  );
};

export default LearningPlan;
