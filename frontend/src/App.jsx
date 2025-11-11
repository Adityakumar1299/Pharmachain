import { BrowserRouter as Router, Routes, Route, useLocation } from "react-router-dom";
import { useEffect } from "react";
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
import PatientForgotPassword from "./pages/Patient/PatientForgotPassword"; // ✅ new import

// Theme
import { ThemeProvider } from "./context/ThemeContext";
import ThemeSwitcher from "./components/ThemeSwitcher";

// ScrollToTop Component
function ScrollToTop() {
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "instant" });
    // use "smooth" instead of "instant" if you want smooth scroll
  }, [pathname]);

  return null;
}

function Layout({ children }) {
  const location = useLocation();

  // Hide Navbar/Footer ONLY on Forgot Password pages
  const hideOnForgot = [
    "/doctor-forgot-password",
    "/pharmacist-forgot-password",
    "/patient-forgot-password" // added patient route
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
        <ScrollToTop />
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
            <Route path="/patient-forgot-password" element={<PatientForgotPassword />} /> {/*  new route */}
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
