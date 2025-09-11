import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import AboutPage from "./pages/About";
import FeaturesPage from "./pages/FeaturesPage";

// Auth Pages
import Signup from "./pages/Auth/Signup";
import Login from "./pages/Auth/Login";
import DoctorForgotPassword from "./pages/Doctor/DoctorForgotPassword";
import PharmacistForgotPassword from "./pages/Pharmacist/PharmacistForgotPassword";

// Theme
import { ThemeProvider } from "./context/ThemeContext";
import ThemeSwitcher from "./components/ThemeSwitcher";

function Layout({ children }) {
  const location = useLocation();

  // Hide Navbar/Footer ONLY on Forgot Password pages
  const hideOnForgot = [
    "/doctor-forgot-password",
    "/pharmacist-forgot-password"
  ];

  const hideLayout = hideOnForgot.includes(location.pathname);

  return (
    <>
      {!hideLayout && <Navbar />}
      {children}
      {!hideLayout && <Footer />}
      {/* Show Theme Switcher globally */}
      {!hideLayout && <ThemeSwitcher />}
    </>
  );
}

function App() {
  return (
    <ThemeProvider>
      <Router>
        <Layout>
          <Routes>
            {/* Home */}
            <Route path="/" element={<Home />} />

            {/* About */}
            <Route path="/about" element={<AboutPage />} />

            {/* Features */}
            <Route path="/features" element={<FeaturesPage />} />

            {/* Auth */}
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/doctor-forgot-password" element={<DoctorForgotPassword />} />
            <Route path="/pharmacist-forgot-password" element={<PharmacistForgotPassword />} />
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
