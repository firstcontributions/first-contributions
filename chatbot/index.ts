import { ChatbotConfig } from './config';
import { processMessage } from './utils';

class Chatbot {
  private config: ChatbotConfig;

  constructor(config: ChatbotConfig) {
    this.config = config;
  }

  public async handleMessage(message: string): Promise<string> {
    return processMessage(message, this.config);
  }
}

export { Chatbot };
