// frontend/src/utils/api.ts
export const interact = async (prompt: string) => {
  const response = await fetch('/api/interact', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt }),
  });
  return response.json();
};

export const getMemory = async () => {
  const response = await fetch('/api/memory');
  return response.json();
};

export const clearMemory = async () => {
  const response = await fetch('/api/memory', {
    method: 'DELETE',
  });
  return response.json();
};