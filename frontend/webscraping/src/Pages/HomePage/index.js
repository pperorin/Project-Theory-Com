import { PageLayout, ProductCard } from '../../components';

const HomePage = () => {
    return (
        <PageLayout>
            <div className="grid grid-cols-4">
                <div className="col-span-1 border-4 border-sky-500 mr-8">Filter panel</div>
                <div className="col-span-3">
                    <div className="grid grid-cols-3 gap-4">
                        <ProductCard />
                        <ProductCard />
                        <ProductCard />
                        <ProductCard />
                    </div>
                </div>
            </div>
        </PageLayout>
    );
};

export default HomePage;
