import { Routes, Route } from 'react-router-dom';

import { HomePage,InfoPage } from './Pages';

function App() {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/stuffinfo/name" element={<InfoPage />} />
        </Routes>
    );
}

export default App;
