import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

let client: ApolloClient<any> | null = null;

export const getClient = () => {
    // create a new client if there's no existing one
    // or if we are running on the server.
    if (!client || typeof window === "undefined") {
      client = new ApolloClient({
        link: new HttpLink({
          uri: process.env.GRAPHQL_URL,
        }),
        cache: new InMemoryCache(),
      });
    }
  
    return client;
  };