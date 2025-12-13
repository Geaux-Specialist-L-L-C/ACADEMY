/// <reference types="react-scripts" />

declare namespace NodeJS {
  interface ProcessEnv {
    readonly REACT_APP_FIREBASE_API_KEY?: string;
    readonly REACT_APP_FIREBASE_AUTH_DOMAIN?: string;
    readonly REACT_APP_FIREBASE_DATABASE_URL?: string;
    readonly REACT_APP_FIREBASE_PROJECT_ID?: string;
    readonly REACT_APP_FIREBASE_STORAGE_BUCKET?: string;
    readonly REACT_APP_FIREBASE_MESSAGING_SENDER_ID?: string;
    readonly REACT_APP_FIREBASE_APP_ID?: string;
    readonly REACT_APP_FIREBASE_MEASUREMENT_ID?: string;
    readonly REACT_APP_SSL_KEY?: string;
    readonly REACT_APP_SSL_CERT?: string;
    readonly REACT_APP_API_URL?: string;
    readonly REACT_APP_OPENAI_API_KEY?: string;
    readonly REACT_APP_SUPABASE_URL?: string;
    readonly REACT_APP_SUPABASE_ANON_KEY?: string;
    readonly REACT_APP_CHESHIRE_API_URL?: string;
    readonly REACT_APP_CHESHIRE_DEBUG?: string;
  }
}
