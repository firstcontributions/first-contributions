export interface ChatbotConfig {
  apiKey: string;
  apiUrl: string;
  timeout: number;
}

const config: ChatbotConfig = {
  apiKey: process.env.CHATBOT_API_KEY || '',
  apiUrl: process.env.CHATBOT_API_URL || 'https://api.example.com',
  timeout: 5000,
};

export default config;
