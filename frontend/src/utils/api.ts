// frontend/src/utils/api.ts
import { Interaction } from './types';

export const interact = async (prompt: string): Promise<{ response: string }> => {
  try {
    const response = await fetch('/api/interact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt }),
    });
    
    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
    }
    
    return response.json();
  } catch (error) {
    console.error('API interaction error:', error);
    throw error;
  }
};

export const getMemory = async (): Promise<Interaction[]> => {
  try {
    const response = await fetch('/api/memory');
    
    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
    }
    
    return response.json();
  } catch (error) {
    console.error('Failed to fetch memory:', error);
    throw error;
  }
};

export const clearMemory = async (): Promise<{ success: boolean }> => {
  try {
    const response = await fetch('/api/memory', {
      method: 'DELETE',
    });
    
    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}: ${response.statusText}`);
    }
    
    return response.json();
  } catch (error) {
    console.error('Failed to clear memory:', error);
    throw error;
  }
};
