import { NextApiRequest, NextApiResponse } from 'next';
import { Chatbot } from '../../chatbot';
import config from '../../chatbot/config';

const chatbot = new Chatbot(config);

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { message } = req.body;
    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    try {
      const response = await chatbot.handleMessage(message);
      return res.status(200).json({ response });
    } catch (error) {
      return res.status(500).json({ error: 'Failed to process message' });
    }
  } else {
    return res.status(405).json({ error: 'Method not allowed' });
  }
}
