import { Routes, Route } from 'react-router-dom';
import { ProductCard } from './components';
import { HomePage,InfoPage } from './Pages';

function App() {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/keyboard/:id" element={<InfoPage />} />
            <Route path="/mouse/:id" element={<InfoPage />} />
            <Route path="/headgear/:id" element={<InfoPage />} />
        </Routes>
    );
}

export default App;
