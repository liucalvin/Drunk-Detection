import "./App.css";
import { useState } from "react";
import { Button, ChakraProvider } from "@chakra-ui/react";
import {
  Center,
  Box,
  FormControl,
  FormLabel,
  FormHelperText,
  Input,
  Text,
  Badge,
  Flex,
} from "@chakra-ui/react";

function App() {
  const [input, setInput] = useState();
  const [response, setResponse] = useState();

  const submitForm = async () => {
    const formData = new FormData();
    formData.append("file", input);

    try {
      console.log(
        "api endpoint:",
        `${process.env.REACT_APP_DRUNK_API_URL}/api/submit/`
      );
      const response = await fetch(
        `${process.env.REACT_APP_DRUNK_API_URL}/api/submit/`,
        {
          method: "POST",
          body: formData,
        }
      );

      if (response) {
        console.log(response);
        const data = await response.json();
        console.log(data.success);
        setResponse(data.success);
        // const data = await response.body.getReader();
        // console.log(data);
      }
    } catch (error) {
      console.log("error!!!");
      console.log(error);
    }
  };

  return (
    <ChakraProvider>
      <Center h="100vh">
        {response ? (
          <>
            <Flex align="baseline" mt={2} flexDirection="column">
              <Text maxW="500px" pt="24px" maxH="400px">
                {response.toString()}
              </Text>
              <Button
                mt="24px"
                onClick={() => {
                  setResponse(null);
                }}
              >
                Reset
              </Button>
            </Flex>
          </>
        ) : (
          <Box p="10" maxW="520px" borderWidth="1px">
            <Flex align="baseline" mt={2}>
              <Badge colorScheme="purple">ATTENTION</Badge>
              <Text
                ml={2}
                textTransform="uppercase"
                fontSize="sm"
                fontWeight="bold"
                color="purple.700"
              >
                Are you drunk???
              </Text>
            </Flex>
            <FormControl>
              <FormLabel>
                Add your drunk/sober photo here to find out NOW!!!
              </FormLabel>
              <Input
                borderWidth="0px"
                type="file"
                onChange={(e) => {
                  console.log(e);
                  console.log(e.target.files[0]);
                  setInput(e.target.files[0]);
                }}
              />
              <FormHelperText>Your data is safe with us ;&#41;</FormHelperText>
            </FormControl>
            <Button
              mt="24px"
              onClick={() => {
                submitForm();
              }}
            >
              Submit
            </Button>
          </Box>
        )}
      </Center>
    </ChakraProvider>
  );
}

export default App;
