import { defineStore } from 'pinia';

export const useWebSocketStore = defineStore({
  id: 'websocket',
  state: () => ({
    ws: null,
    messages: [],
  }),
  actions: {
    connect(url) {
      this.ws = new WebSocket(url);

      this.ws.onopen = (event) => {
        console.log('WebSocket connected', event);
      };

      this.ws.onmessage = (event) => {
        this.messages.push(event.data);
      };

      this.ws.onclose = () => {
        console.log('WebSocket closed');
      };
    },
    sendMessage(message) {
      if (this.ws && this.ws.readyState === WebSocket.OPEN) {
        this.ws.send(message);
      }
    },
    disconnect() {
      if (this.ws) {
        this.ws.close();
      }
    },
  },
});
