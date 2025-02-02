import { BaseApiClient } from "./_base";

class ApiClient extends BaseApiClient {
  constructor() {
    super(import.meta.env.VITE_API_URL || "", "access_token");
  }
}

const client = new ApiClient();
export const api = client.api;
