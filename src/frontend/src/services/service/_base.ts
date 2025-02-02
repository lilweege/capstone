// src/api/BaseApiClient.ts
import axios, {
  AxiosInstance,
  AxiosError,
  InternalAxiosRequestConfig,
  AxiosResponse,
  AxiosHeaders,
} from "axios";

export class BaseApiClient {
  public api: AxiosInstance;

  constructor(private baseUrl: string, private tokenPrefix: string) {
    this.api = axios.create({
      baseURL: this.baseUrl,
    });
    this.setupInterceptors();
  }

  private setupInterceptors(): void {
    // Request interceptor
    this.api.interceptors.request.use(
      (config: InternalAxiosRequestConfig): InternalAxiosRequestConfig => {
        // Grab the token from localStorage
        const token = localStorage.getItem(this.tokenPrefix);
        if (token) {
          // If headers is an AxiosHeaders instance, use its set() method
          if (config.headers instanceof AxiosHeaders) {
            config.headers.Authorization = `Bearer ${token}`;
          }
        }

        return config;
      },
      (error: AxiosError) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor
    this.api.interceptors.response.use(
      (response: AxiosResponse) => {
        return response;
      },
      (error: AxiosError) => {
        // Example: if 401, redirect or handle unauthorized
        if (error.response?.status === 401) {
          // e.g. window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }
}
