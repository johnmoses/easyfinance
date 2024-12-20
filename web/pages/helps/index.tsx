import { GetStaticProps, NextPage } from "next";
import { addApolloState, initializeApollo } from "@/clients/apollo";
import Layout from "@/components/layout";
import { List } from "@/modules/helps/List";
// import { usePageAnalytics } from "@/hooks";

const HelpsPage: NextPage = () => {
  // usePageAnalytics();

  return (
    <Layout title="Help Center">
      <List />
    </Layout>
  );
};

export const getStaticProps: GetStaticProps = async () => {
  const apolloClient = initializeApollo();

  return addApolloState(apolloClient, {
    props: {},
  });
};

export default HelpsPage;
