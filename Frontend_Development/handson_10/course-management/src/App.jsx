import ErrorBoundary from "./components/ErrorBoundary";

import CoursesPage from "./pages/CoursesPage";

function App() {
  return (
    <ErrorBoundary>
      <CoursesPage />
    </ErrorBoundary>
  );
}

export default App;