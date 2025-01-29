# Frontend Project

This is the frontend for your React-based project, using Vite as the build tool and Tailwind CSS for styling.

## Folder Structure

```
- src/
  - components/      # Reusable UI components
  - hooks/           # Custom React hooks
  - lib/             # Utility functions or libraries
  - pages/           # Page components
  - App.tsx          # Main application component
  - App.css          # Global styles
  - index.css        # Additional global styles
  - main.tsx         # Application entry point
  - vite-env.d.ts    # TypeScript environment variables

- .env               # Environment variables (not committed)
- .gitignore         # Files to be ignored by Git
- components.json    # Component metadata/configuration
- eslint.config.js   # ESLint configuration
- index.html         # Main HTML file
- package.json       # Project dependencies and scripts
- package-lock.json  # Dependency lock file
- postcss.config.js  # PostCSS configuration
- README.md          # Project documentation
- tailwind.config.ts # Tailwind CSS configuration
- tsconfig.app.json  # TypeScript config for the app
- tsconfig.json      # TypeScript base configuration
- tsconfig.node.json # TypeScript config for Node.js
- vite.config.ts     # Vite configuration
```

## Environment Variables

Ensure you create a `.env` file at the root of your project with the following variables:

| Variable               | Description                     |
| ---------------------- | ------------------------------- |
| `VITE_AUTH0_DOMAIN`    | Auth0 domain for authentication |
| `VITE_AUTH0_CLIENT_ID` | Auth0 client ID                 |

## Getting Started

### Prerequisites

- Node.js (latest LTS version recommended)
- npm or yarn

### Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Create a `.env` file and add your environment variables.
4. Start the development server:
   ```sh
   npm run dev
   ```
