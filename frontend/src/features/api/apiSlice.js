// src/features/api/apiSlice.js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const apiSlice = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: import.meta.env.VITE_API_URL,
  }),
  endpoints: (builder) => ({
    getTrains: builder.query({
      query: () => '/trains/',
    }),
    createTrain: builder.mutation({
      query: (newTrain) => ({
        url: '/trains/',
        method: 'POST',
        body: newTrain,
      }),
    }),
    deleteTrain: builder.mutation({
      query: (trainId) => ({
        url: `/trains/${trainId}/`,
        method: 'DELETE',
      }),
    }),
    editTrain: builder.mutation({
      query: ({ trainId, updatedTrain }) => ({
        url: `/trains/${trainId}/`,
        method: 'PUT',
        body: updatedTrain,
      }),
    }),
    getCarriages: builder.query({
      query: () => '/carriages/',
    }),
      createCarriage: builder.mutation({
        query: (newCarriage) => ({
          url: '/carriages/',
          method: 'POST',
          body: newCarriage,
        }),
      }),
      deleteCarriage: builder.mutation({
        query: (carriageId) => ({
          url: `/carriages/${carriageId}/`,
          method: 'DELETE',
        }),
      }),
      editCarriage: builder.mutation({
        query: ({ carriageId, updatedCarriage }) => ({
          url: `/carriages/${carriageId}/`,
          method: 'PUT',
          body: updatedCarriage,
        }),
      }),
  })
});

export const { useGetItemsQuery, useCreateItemMutation,useGetTrainsQuery,useCreateTrainMutation,useDeleteTrainMutation,useEditTrainMutation,useEditCarriageMutation,useDeleteCarriageMutation,
useCreateCarriageMutation,useGetCarriagesQuery
 } = apiSlice;